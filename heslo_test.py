from unittest import TestCase


class hesloTest(TestCase):

def validni_heslo(heslo: str) -> str:
    """

    :param heslo: Heslo musí obsahovat 5 a více znaků
    :return: Heslo je neplatné – je příliš krátké.
    """


            if len(heslo) <= 5:
                return "Heslo je neplatné – je příliš krátké."

            # musí obsahovat alespoň jednu číslici
            if not any(char.isdigit() for char in heslo):
                return "Heslo je neplatné – chybí číslice."


            return "Heslo je platné."

        # pár testů
        hesla = ["abc", "abcdef", "abc123", "heslo9", "12345"]
        for h in hesla:
            print(f"{h}: {validni_heslo(h)}")

