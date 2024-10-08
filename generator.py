import json

anime_list = []

def get_score_by_text(text):
    index_symbol = text.find("✦")
    if index_symbol == -1:
        return None
    try:
        return float(text[index_symbol+2:index_symbol+6])
    except ValueError:
        return None



def generate_by_anime(anime):
    text = anime["text"]
    text = text if text is not None else ""
    #
    text_score = get_score_by_text(text)
    if text_score is None:
        score = anime["score"]
    else:
        score = text_score
    #
    anime_list.append({
        "ID" : anime["target_id"],
        "SCORE" : int(score * 10)
    })
    
def generate_css(id, score):
    with open("output_css.txt", "a", encoding="utf-8") as f:
        f.write(f'''.c-column.user_rate[data-target_id="{id}"] {{
    order: -{score};
}}\n''')
        f.write(f'''.list-groups .b-table.list-lines tbody.entries tr[data-target_id="{id}"] {{
    order: -{score};
}}\n''')

def main_anime():
    
    with open('Hayart_animes.json', 'r', encoding='utf-8') as f:
        hayart_animes = json.load(f)

    for anime in hayart_animes:
        if anime["status"] == "completed":
            generate_by_anime(anime)

    for anime in sorted(anime_list, key=lambda anime: anime["SCORE"], reverse=True):
        generate_css(anime["ID"], anime["SCORE"])
        

    


main_anime()


