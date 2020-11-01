fake_db = {
    '/team/members/': {
        'page_title': 'Our Members',
        'page_details': 'Details about our members...',
    },

    '/team/goals/': {
        'page_title': 'Our Goals',
        'page_details': 'Details about our goals...',
    },
}

def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.lower().strip()
    url = '/' + url.lstrip('/')

    page = fake_db.get(url, {})
    return page

