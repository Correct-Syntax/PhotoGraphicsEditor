## This code is Copyright (C) 2019 Noah Rahm
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the GNU General Public License as published by 
## the Free Software Foundation; either version 3 of the License, 
## or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty 
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License 
## along with this program. If not, see: http://www.gnu.org/licenses/
##
## Contributor(s): Noah Rahm
## This code of this algorithm is Copyright (c) 2013 Mikita Hradovich

import random, math
from PIL import Image


class Perlin_Noise(object):
    def __init__(self, imagesize):
        self.imageSizex = imagesize[0]
        self.imageSizey = imagesize[1]
        self.gradientNumber = 256

        self.grid = [[]]
        self.gradients = []
        self.permutations = []
        self.img = {}

        self.__generate_gradient_vectors()
        self.__normalize_gradient_vectors()
        self.__generate_permutations_table()

    def __generate_gradient_vectors(self):
        for i in range(self.gradientNumber):
            while True:
                x, y = random.uniform(-1, 1), random.uniform(-1, 1)
                if x * x + y * y < 1:
                    self.gradients.append([x, y])
                    break

    def __normalize_gradient_vectors(self):
        for i in range(self.gradientNumber):
            x, y = self.gradients[i][0], self.gradients[i][1]
            length = math.sqrt(x * x + y * y)
            self.gradients[i] = [x / length, y / length]

    ## The modern version of the Fisher-Yates shuffle
    def __generate_permutations_table(self):
        self.permutations = [i for i in range(self.gradientNumber)]
        for i in reversed(range(self.gradientNumber)):
            j = random.randint(0, i)
            self.permutations[i], self.permutations[j] = \
                self.permutations[j], self.permutations[i]

    def get_gradient_index(self, x, y):
        return self.permutations[(x + self.permutations[y % self.gradientNumber]) % self.gradientNumber]

    def perlin_noise(self, x, y):
        qx0 = int(math.floor(x))
        qx1 = qx0 + 1

        qy0 = int(math.floor(y))
        qy1 = qy0 + 1

        q00 = self.get_gradient_index(qx0, qy0)
        q01 = self.get_gradient_index(qx1, qy0)
        q10 = self.get_gradient_index(qx0, qy1)
        q11 = self.get_gradient_index(qx1, qy1)

        tx0 = x - math.floor(x)
        tx1 = tx0 - 1

        ty0 = y - math.floor(y)
        ty1 = ty0 - 1

        v00 = self.gradients[q00][0] * tx0 + self.gradients[q00][1] * ty0
        v01 = self.gradients[q01][0] * tx1 + self.gradients[q01][1] * ty0
        v10 = self.gradients[q10][0] * tx0 + self.gradients[q10][1] * ty1
        v11 = self.gradients[q11][0] * tx1 + self.gradients[q11][1] * ty1

        wx = tx0 * tx0 * (3 - 2 * tx0)
        v0 = v00 + wx * (v01 - v00)
        v1 = v10 + wx * (v11 - v10)

        wy = ty0 * ty0 * (3 - 2 * ty0)
        return (v0 + wy * (v1 - v0)) * 0.5 + 1

    def make_texture(self, texture=None):
        if texture is None:
            texture = self.cloud

        noise = {}
        max = min = None
        for i in range(self.imageSizex):
            for j in range(self.imageSizey):
                value = texture(i, j)
                noise[i, j] = value
                
                if max is None or max < value:
                    max = value

                if min is None or min > value:
                    min = value

        for i in range(self.imageSizex):
            for j in range(self.imageSizey):
                self.img[i, j] = (int) ((noise[i, j] - min) / (max - min) * 255 )

    def fractal_brownian_motion(self, x, y, func):
        octaves = 12
        amplitude = 1.0
        frequency = 1.0 / self.imageSizex
        persistence = 0.5
        value = 0.0
        for k in range(octaves):
            value += func(x * frequency, y * frequency) * amplitude
            frequency *= 2
            amplitude *= persistence
        return value

    def cloud(self, x, y, func=None):
        if func is None:
            func = self.perlin_noise

        return self.fractal_brownian_motion(8 * x, 8 * y, func)

    def wood(self, x, y, noise=None):
        if noise is None:
            noise = self.perlin_noise

        frequency = 1.0 / self.imageSizex
        n = noise(4 * x * frequency, 4 * y * frequency) * 10
        return n - int(n)

    def marble(self, x, y, noise=None):
        if noise is None:
            noise = self.perlin_noise

        frequency = 1.0 / self.imageSizex
        n = self.fractal_brownian_motion(8 * x, 8 * y, self.perlin_noise)
        return (math.sin(16 * x * frequency + 4 * (n - 0.5)) + 1) * 0.5


def create_perlincloud_noise(self, dimensions):
    noise = Perlin_Noise(dimensions)
    noise.make_texture(texture=noise.cloud)
    img = Image.new("L", dimensions)
    pixels = img.load()
    for i in range(0, dimensions[0]):
       for j in range(0, dimensions[1]):
            c = noise.img[i, j]
            pixels[i, j] = c

    return img

def create_perlinmarble_noise(self, dimensions):
    noise = Perlin_Noise(dimensions)
    noise.make_texture(texture=noise.marble)
    img = Image.new("L", dimensions)
    pixels = img.load()
    for i in range(0, dimensions[0]):
       for j in range(0, dimensions[1]):
            c = noise.img[i, j]
            pixels[i, j] = c

    return img

def create_perlinwood_noise(self, dimensions):
    noise = Perlin_Noise(dimensions)
    noise.make_texture(texture=noise.wood)
    img = Image.new("L", dimensions)
    pixels = img.load()
    for i in range(0, dimensions[0]):
       for j in range(0, dimensions[1]):
            c = noise.img[i, j]
            pixels[i, j] = c

    return img
