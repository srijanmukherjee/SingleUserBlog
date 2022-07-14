def convert_to_slug(title: str) -> str:
    title_without_sp_chars = ''.join([c for c in title if c.isalnum() or c is ' '])
    slug = '-'.join([word.strip() for word in title_without_sp_chars.strip().lower().split()])
    return slug
