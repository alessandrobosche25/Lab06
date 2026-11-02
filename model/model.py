from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        conn = None
        cursor = None

        try:
            conn = get_connection()

            if conn is None:
                return None

            cursor = conn.cursor()

            query = """
                SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                FROM strumento
                ORDER BY codice
            """

            cursor.execute(query)

            risultati = cursor.fetchall()

            strumenti = []

            for riga in risultati:
                s = Strumento(
                    riga[0],
                    riga[1],
                    riga[2],
                    riga[3],
                    riga[4],
                    riga[5]
                )

                strumenti.append(s)

            return strumenti

        except Exception as e:
            print(f"Errore nel recupero degli strumenti: {e}")
            return None

        finally:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        conn = None
        cursor = None

        try:
            conn = get_connection()

            if conn is None:
                return None

            cursor = conn.cursor()

            query = """
                SELECT codice, tipo, marca, anno_acquisto, valore, disponibile
                FROM strumento
                WHERE tipo = %s
                ORDER BY codice
            """

            cursor.execute(query, (tipo.strip(),))

            risultati = cursor.fetchall()

            strumenti = []

            for riga in risultati:
                s = Strumento(
                    riga[0],
                    riga[1],
                    riga[2],
                    riga[3],
                    riga[4],
                    riga[5]
                )

                strumenti.append(s)

            return strumenti

        except Exception as e:
            print(f"Errore nella ricerca degli strumenti: {e}")
            return None

        finally:
            if cursor is not None:
                cursor.close()

            if conn is not None:
                conn.close()
