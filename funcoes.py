import io
import sys
from functools import wraps

# Decorador para capturar a saída de exec()
def captura_saida(func):
    @wraps(func)
    def wrapper(codigo):
        # Criar um buffer para capturar a saída
        buffer = io.StringIO()
        saida_original = sys.stdout
        sys.stdout = buffer

        try:
            # Executar a função e capturar a saída
            func(codigo)
        except Exception as e:
            print(f"Erro ao executar o código: {e}")
        finally:
            # Restaurar a saída padrão original
            sys.stdout = saida_original

        # Obter a saída capturada como uma string
        return buffer.getvalue()
    return wrapper

 
# Assim como a função exec() a função info() não retorna valores, é necessário capturar sua saída

def retonar_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)

    return buffer.getvalue()