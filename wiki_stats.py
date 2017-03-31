#!/usr/bin/python3

import os
import sys
import math
import timeit
import array

import statistics


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)
        filename.self = open("cities.txt",'r')

        with open(filename) as f:
            (n, _nlinks) = map(int, f.readlines().split()) # TODO: прочитать из файла
            self.blablabla = n
            self._titles = []
            self._sizes = array.array('l', [0]*n)
            self._links = array.array('l', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('l', [0]*(n+1))

            l = 0
            for i in range(n):
                title = f.readline()
                self._titles.append(title)

                sz, redr,numlinks = map(int, f.readline().split())
                self._sizes[i] = sz
                self._redirect[i] = redr

                self._offset[i] = l
                for j in range(numlinks):
                    self._links[l] = int(f.readline())
                    l += 1

            self._offset[i] = l
            #self._offset[i] = self.offset[i-1] + l



        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id+1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        self.titles = self._titles[1]

    def get_number_of_pages(self):
        return self.blablabla

    def is_redirect(self, _id):
        return bool(self.get_id(_id))

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    def bfs_path(_from,_to):
        Q = array.array('L',[0]*wg.get_number_of_pages())
        parent = array.array('L', [-1]*wg.get_number_of_pages())
        dist = array.array('L', [-1]*wg.get_number_of_pages())

        first = 0
        last = 1
        print('Let_s go')

        Q[first] = wg.get_id(_from)
        parent[[Q[first]]] = -1
        dist[[Q[last]]] = 0

        while first < last:
            for neib in wg.get_links_from(Q[first]):
                if dist[neib] == -1:
                    dist[neib] = dist[Q[first]] + 1
                    parent[neib] = Q[first]
                    if neib == wg.get_id(_to):
                        return parent
                    Q[last] = neib
                    last += 1
            first += 1

        parents = bfs_path("Python", "Список_файловых_систем")
        idx = wg.get_id("Список_файловых_систем")
        path = []
        while idx != -1:
            path.append(wg.get_title(idx))
            idx = parents[idx]

        print("Put naiden:")
        print('\n'.join(path[::-1]))
