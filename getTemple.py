import requests
import re
import csv


def getTem(province):
    url_dict = {
        "prayao": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดพะเยา",
        "pattani": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดปัตตานี",
        "Ayutthaya": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดพระนครศรีอยุธยา",
        "PrachinBuri": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดปราจีนบุรี"
    }
    if province not in url_dict:
        return None
    url = url_dict[province]
    if province == "prayao":
        response = requests.get(url)
        html_content = response.text
        li_match = re.findall('>(.*?)<', html_content)
        li_match = [e for e in li_match if re.match('^วัด', e)]
        li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ใน)', e)]
        li_match = [e for e in li_match if re.match('(?!วัดราษฏร์มหา)', e)]
        li_match = [e for e in li_match if re.match(
            '(?!วัดราษฏร์ธรรม)', e)]

        li_match = [re.sub('\([^)]*\)', '', e) for e in li_match]

        li_match = li_match[:-4]
        li_match = list(set(li_match))
        return li_match
    elif province == "pattani":
        response = requests.get(url).text
        li = re.findall('>(.*?)<', response)
        li = [i for i in li if re.match('^วัด', i)]
        li = [i for i in li if re.match('(?!วัดราษฏร์)', i)]
        for i in range(len(li)):
            li[i] = re.sub(r'\s*\([^)]*\)\s*$', '', li[i])
        result = li[:-4]
        return result
    elif province == "Ayutthaya":
        response = requests.get(url)
        html_content = response.text

        li_match = re.findall('>(.*?)<', html_content)
        li_match = [e for e in li_match if re.match('^วัด', e)]
        li_match = [e for e in li_match if re.match('(?!วัดราษฏร์ใน)', e)]
        li_match = [e for e in li_match if re.match('(?!วัดราษฎร์ใน)', e)]
        li_match = [e for e in li_match if re.match('(?!วัดราษฏร์มหา)', e)]
        li_match = [e for e in li_match if re.match('(?!วัดราษฎร์มหา)', e)]

        li_match = [e for e in li_match if re.match('(?!วัดใน)', e)]
        li_match = [e for e in li_match if re.match('(?!วัดหลวงใน)', e)]
        li_match = [e for e in li_match if re.match('(?!วัดไทย)', e)]
        li_match = [e for e in li_match if re.match(
            '(?!วัดหน้าพระเมรุ)', e)]
        li_match = [e for e in li_match if re.match(
            '(?!วัดราษฎร์ธรรม)', e)]

        li_match = [re.sub('\([^)]*\)', '', e) for e in li_match]
        li_match = [re.sub('ตำบล.*?', '', e) for e in li_match]
        li_match = [re.sub(' หรือ', '', e) for e in li_match]

        li_match = list(set(li_match))
        li_match.sort()
        li_match = li_match[1:]

        return li_match

    elif province == "PrachinBuri":
        response = requests.get(url)
        html_content = response.text
        li = re.findall('>(.*?)<', html_content)
        li = [result for result in li if re.match('(^วัด)', result)]
        li = [result for result in li if re.match('(?!วัดราษฏร์)', result)]

        temple_names = []
        pattern = re.compile(r"\S+")
        for temple in li:
            match = pattern.search(temple)
            if match:
                temple_names.append(match.group(0))

        temple_name = temple_names[:-4]
        return temple_name
