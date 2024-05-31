import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


# My tests
@pytest.mark.api
def test_get_emoji(github_api):
    emojis = github_api.get_emoji()
    assert "100" in emojis, "Emoji '100' not found in the response"
    assert emojis["100"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f4af.png?v8",\
        "URL for emoji '100' does not match"
    # Проверяем наличие "100" emojis
@pytest.mark.api
def test_get_emoji_not_present(github_api):
    emojis = github_api.get_emoji()
    assert "100A" not in emojis, "Emoji '100A' found in the response, but it should not be present"
    # Проверяем отсутствие "100А" emojis