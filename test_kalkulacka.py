from unittest import TestCase

from kalkulacka import kalkulacka


class Testkalkulacka(TestCase):
    def test_secti(self):
        """
        test součtu
        :return:
        """
        kal = kalkulacka()
        self.assertEqual(4, kalkulacka().secti(3, 1), )
        self.assertEqual(-4, kalkulacka().secti(-8, 4), )


class Testkalkulacka2(TestCase):
    """
    Test odečtu
    """

    def test_odecti(self):
        self.assertEqual(2, kalkulacka().odecti(3, 1), )
        self.assertEqual(4, kalkulacka().odecti(-8, 4), )


class Testkalkulacka(TestCase):
    """
    Test násobení
    """
    def test_vynásob(self):
        self.assertEqual(4,kalkulacka().vynásob(1,4))
        self.assertEqual(20,kalkulacka().vynásob(5,4))

class Testkalkulacka(TestCase):
    def test_vyděl(self):
        """
        test dělení
        :return:
        """
        self.assertEqual(1, kalkulacka().vyděl(3, 3))
        self.assertEqual(2, kalkulacka().vyděl(10, 5))
