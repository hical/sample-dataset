#!/usr/bin/env python3
""" Preprocess the sample dataset
Usage: python process.py athome4_sample.tgz
"""

import sys
import os
import argparse
import tarfile
from io import BytesIO
from tqdm import tqdm

def get_paragraphs(filecontent):
    paragraphs = filecontent.split('\n\n')
    final_paragraphs = []
    cur_para = []
    for idx, para in enumerate(paragraphs):
        para = para.strip()
        if len(para) <= 0:
            continue
        if len(''.join(cur_para)) < 100:
            cur_para.append(para)
        else:
            final_paragraphs.append('\n\n'.join(cur_para))
            cur_para = [para]

    if len(''.join(cur_para)) > 0 and len(''.join(cur_para)) < 100 and final_paragraphs:
        final_paragraphs[-1] += '\n\n' + '\n\n'.join(cur_para)

    return final_paragraphs


def cleandoc(content):
    ret = []
    for line in content.split('\n'):
        ret.append(line.strip())
    return '\n'.join(ret)


def process(input_corpus):
    output_file = os.path.splitext(os.path.basename(input_corpus))[0] + '_para.tgz'
    with tarfile.open(input_corpus) as tarf, tarfile.open(output_file, 'w:gz') as out:
        for tarinfo in tqdm(tarf):
            if not tarinfo.isfile():
                continue
            name = tarinfo.name
            filecontent = tarf.extractfile(tarinfo).read().decode('ascii', 'ignore').replace('\r', '')
            filecontent = cleandoc(filecontent)
            paragraphs = get_paragraphs(filecontent)

            for idx, para in enumerate(paragraphs):
                para_name = '%s.%d' % (name, idx)
                content = BytesIO()
                content.write(para.strip().encode())
                newfile = tarfile.TarInfo(para_name)
                newfile.size = content.tell()
                content.seek(0)
                out.addfile(newfile, content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('corpus')
    args = parser.parse_args()
    process(args.corpus)
