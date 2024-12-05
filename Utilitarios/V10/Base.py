import inspect

class Base:
    @staticmethod
    def dec_bin(numero):
        if isinstance(numero, float):
            parte_inteira = int(abs(numero))
            parte_decimal = abs(numero) - parte_inteira
            bin_inteira = bin(parte_inteira)[2:]
            bin_decimal = []
            while parte_decimal > 0 and len(bin_decimal) < 20:  # Limite para precisão
                parte_decimal *= 2
                bit = int(parte_decimal)
                bin_decimal.append(str(bit))
                parte_decimal -= bit
            resultado = f"{'-' if numero < 0 else ''}{bin_inteira}.{''.join(bin_decimal)}"
        else:
            resultado = bin(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else bin(int(numero))[2:]
        return resultado

    @staticmethod
    def dec_oct(numero):
        if isinstance(numero, float):
            parte_inteira = int(abs(numero))
            parte_decimal = abs(numero) - parte_inteira
            oct_inteira = oct(parte_inteira)[2:]
            oct_decimal = []
            while parte_decimal > 0 and len(oct_decimal) < 20:  # Limite para precisão
                parte_decimal *= 8
                bit = int(parte_decimal)
                oct_decimal.append(str(bit))
                parte_decimal -= bit
            resultado = f"{'-' if numero < 0 else ''}{oct_inteira}.{''.join(oct_decimal)}"
        else:
            resultado = oct(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else oct(int(numero))[2:]
        return resultado

    @staticmethod
    def dec_hex(numero):
        if isinstance(numero, float):
            import struct
            hexadecimal = struct.pack('>f', numero).hex()  # IEEE 754
            resultado = f"0x{hexadecimal}"
        else:
            resultado = hex(int(numero) & 0xFFFFFFFF)[2:] if numero < 0 else hex(int(numero))[2:]
        return resultado

    @staticmethod
    def bin_dec(binario):
        """Converte um número binário para decimal."""
        return int(binario, 2)

    @staticmethod
    def oct_dec(octal):
        """Converte um número octal para decimal."""
        return int(octal, 8)

    @staticmethod
    def hex_decl(hexadecimal):
        """Converte um número hexadecimal para decimal."""
        return int(hexadecimal, 16)

    @staticmethod
    def dec_para_qualquer_base(numero, base):
        """Converte um número decimal para qualquer base (2 a 36)."""
        if not (2 <= base <= 36):
            raise ValueError("Base deve estar entre 2 e 36")
        caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while numero > 0:
            resultado = caracteres[numero % base] + resultado
            numero //= base
        return resultado or "0"

    @staticmethod
    def qualquer_base_para_dec(numero, base):
        """Converte um número de qualquer base (2 a 36) para decimal."""
        if not (2 <= base <= 36):
            raise ValueError("Base deve estar entre 2 e 36")
        return int(numero, base)

    def raiz_quadrada(self, num):
        """Calcula a raiz quadrada de um número usando o método de Newton."""
        if num < 0:
            return complex(0, abs(num) ** 0.5)  # Para números negativos, retorna a parte imaginária
        x = num
        y = (x + 1) / 2
        while y < x:
            x = y
            y = (x + num / x) / 2
        return x

    def saida(self, num):
        print(f"Sistemas: Decimal: {num}, Octal: {self.dec_oct(num)}, Hexadecimal: {self.dec_hex(num)}, Binário {self.dec_bin(num)}")

    def __def__():
        nome_funcao = inspect.currentframe().f_code.co_name
        print("O nome desta função é:", nome_funcao)

