import string


def create_alphabet(alphabet):
    global ALPHABET, LETTER_DICT, SIZE
    ALPHABET = alphabet
    SIZE = len(alphabet)
    LETTER_DICT = {ALPHABET[i]: i for i in range(SIZE)}


class Rotor:

    def __init__(self, path_disk):
        self.disk = []
        with open(path_disk) as disk_file:
            for line in disk_file:
                self.disk.append(int(line.strip()))
        self.disk_ini = list(self.disk)

    def reset(self):
        self.disk = list(self.disk_ini)

    def rotate_disk(self):
        newdisk = [self.disk[(i - 1) % SIZE] for i in range(SIZE)]
        self.disk = newdisk

    def get(self, number):
        if number > SIZE - 1 or number < 0:
            return None
        return self.disk[number]

    def get_out(self, number):
        return self.disk.index(number)


class Reflector:

    def __init__(self, path_disk):
        self.refl = {}
        with open(path_disk) as disk_file:
            num1 = 0
            for line in disk_file:
                num2 = int(line.strip())
                self.refl[num1] = num2
                self.refl[num2] = num1
                num1 += 1

    def get(self, number):
        return self.refl.get(number)


class Encoder:

    def __init__(self, path_rotors, path_reflectors):
        self.pos = 0
        self.rotors = []
        self.size = len(path_rotors)
        for path in path_rotors:
            self.rotors.append(Rotor(path))
        self.refl = Reflector(path_reflectors)

    def reset(self):
        self.pos = 0
        for rot in self.rotors:
            rot.reset()

    def transform_letter(self, num):
        aux = num
        for rot in self.rotors:
            aux = rot.get(aux)
        aux = self.refl.get(aux)
        for rot in reversed(self.rotors):
            aux = rot.get_out(aux)
        return aux

    def rotate_disks(self):
        self.pos += 1
        self.rotors[0].rotate_disk()
        for i in range(1, self.size):
            if self.pos % (SIZE**i) == 0:
                self.rotors[i].rotate_disk()
        self.pos = self.pos % (SIZE**(self.size - 1))

    def encrypt(self, text):
        out = []
        self.reset()

        for let1 in text:
            num1 = LETTER_DICT.get(let1)
            if num1 is None:
                raise ValueError(
                    'El caracter %s no esta en el alfabeto' % let1)
            num2 = self.transform_letter(num1)
            let2 = ALPHABET[num2]
            self.rotate_disks()
            out.append(let2)

        return ''.join(out)

    def write_text(self, path_in, path_out):
        with open(path_out, 'w') as out:
            with open(path_in) as inp:
                for line in inp:
                    encrypted = self.encrypt(line.strip())
                    out.write(encrypted + '\n')


if __name__ == '__main__':
    rots = ['files\\rotor1.txt', 'files\\rotor2.txt', 'files\\rotor3.txt']
    refl = 'files\\reflector.txt'

    # entrega el alfabeto
    create_alphabet((list(string.ascii_lowercase)))

    enc = Encoder(rots, refl)

    # encriptando con la funcion directamente
    a = enc.encrypt('hola')
    b = enc.encrypt(a)
    print(a, b)

    # leyendo desde el archivo
    enc.write_text('files\\input.txt', 'files\\output.txt')
