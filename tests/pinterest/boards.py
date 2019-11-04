from src.services.pinterest.pinterest import Pinterest


class TestBoards:
    def test_create_board(self):
        p = Pinterest()
        r, d = p.post('/boards/', {})
        p.verify(r.status_code == 400)
        p.is_failed()

    def test_get_boards(self):
        p = Pinterest()
        r, d = p.get('/me/boards/')
        p.verify(r.status_code == 200)
        p.verify(d['data'])
        p.is_failed()
