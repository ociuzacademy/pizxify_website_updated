from PIL import Image


def crop_to_ratio(img, target_ratio):

    w, h = img.size

    current_ratio = w / h

    if current_ratio > target_ratio:

        new_w = int(h * target_ratio)

        left = (w - new_w) // 2

        img = img.crop(
            (
                left,
                0,
                left + new_w,
                h
            )
        )

    else:

        new_h = int(w / target_ratio)

        top = (h - new_h) // 2

        img = img.crop(
            (
                0,
                top,
                w,
                top + new_h
            )
        )

    return img


def prepare_image(path, width, height):

    img = Image.open(path)

    if img.mode != "RGB":
        img = img.convert("RGB")

    target_ratio = width / height

    img = crop_to_ratio(
        img,
        target_ratio
    )

    img = img.resize(
        (width, height),
        Image.LANCZOS
    )

    return img



def fit_full_page(path, canvas_width=1800, canvas_height=1200):
    """
    Fits the image fully inside the canvas without cropping, preserving
    aspect ratio and orientation. Canvas orientation auto-switches to
    portrait if the photo is portrait, so nothing gets letterboxed
    more than necessary.
    """
    img = Image.open(path)

    if img.mode != "RGB":
        img = img.convert("RGB")

    w, h = img.size

    # Swap canvas to match the photo's orientation
    if h > w:
        canvas_width, canvas_height = canvas_height, canvas_width

    img_ratio = w / h
    canvas_ratio = canvas_width / canvas_height

    if img_ratio > canvas_ratio:
        # image is relatively wider than canvas -> fit to width
        new_w = canvas_width
        new_h = int(canvas_width / img_ratio)
    else:
        # image is relatively taller than canvas -> fit to height
        new_h = canvas_height
        new_w = int(canvas_height * img_ratio)

    img = img.resize((new_w, new_h), Image.LANCZOS)

    canvas = Image.new("RGB", (canvas_width, canvas_height), "white")

    paste_x = (canvas_width - new_w) // 2
    paste_y = (canvas_height - new_h) // 2

    canvas.paste(img, (paste_x, paste_y))

    return canvas


def create_collage(photo_paths, output_path):

    count = len(photo_paths)

    if count == 0:
        return

    # =========================
    # 1 PHOTO — full page, no crop, original aspect ratio preserved
    # =========================
    if count == 1:
        canvas = fit_full_page(photo_paths[0], 1800, 1200)
        canvas.save(output_path, quality=95)
        return

    # =========================
    # MAIN CANVAS (2+ photos — unchanged, still grid-cropped)
    # =========================
    canvas = Image.new("RGB", (1800, 1200), "white")

    if count == 2:
        img1 = prepare_image(photo_paths[0], 850, 1100)
        img2 = prepare_image(photo_paths[1], 850, 1100)
        canvas.paste(img1, (50, 50))
        canvas.paste(img2, (900, 50))

    elif count == 3:
        img1 = prepare_image(photo_paths[0], 900, 1100)
        img2 = prepare_image(photo_paths[1], 800, 540)
        img3 = prepare_image(photo_paths[2], 800, 540)
        canvas.paste(img1, (20, 50))
        canvas.paste(img2, (950, 50))
        canvas.paste(img3, (950, 610))

    elif count == 4:
        positions = [(0, 0), (900, 0), (0, 600), (900, 600)]
        for path, pos in zip(photo_paths[:4], positions):
            img = prepare_image(path, 900, 600)
            canvas.paste(img, pos)

    else:
        positions = [(0, 0), (900, 0), (0, 600), (900, 600)]
        for path, pos in zip(photo_paths[:4], positions):
            img = prepare_image(path, 900, 600)
            canvas.paste(img, pos)

    canvas.save(output_path, quality=95)