def convert_to_slug(title: str) -> str:
    slug = '-'.join([word.strip() for word in title.strip().lower().split()])
    return slug
