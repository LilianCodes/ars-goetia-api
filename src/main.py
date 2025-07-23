from fastapi import FastAPI
from pathlib import Path
import json
import random

app = FastAPI()
DATA_PATH = Path("goetia.json")


def load_goetia():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def error_handling(message: str, q: str = ""):
    return {
        "error": message,
        "query": q,
        "results": []
    }

goetia = load_goetia()

@app.get("/", summary="The root of the API.")
def root():
    return {
        "introduction": "Welcome to the Ars Goetia REST API!",
        "message-one": "This API holds all information on the 72 Goetic Demons.",
        "message-two": "AGAPI was created from a love of occult topics and there were no other APIs with this information freely available. So I figured why not?",
        "message-three": "Feel free to peruse endpoints at your leisure! By the way, all endpoints are GET only.",
        "endpoints": {
            "goetia": "All Goetic information.",
            "goetia/random": "A random Goetic.",
            "goetia/id": "All Goetics by ID number.",
            "goetia/id/{id}": "Specific Goetic by ID number.",
            "goetia/name": "All Goetics by name.",
            "goetia/name/{name}": "Specific Goetic by name.",
            "goetia/alt-names": "Alternate names that the Goetics go by.",
            "goetia/alt-names/{name}": "Specific Goetic by alternate name.",
            "goetia/rank-name{rank-name}": "Goetic by rank name. (King, President, Earl, Duke, etc)",
            "goetia/ruling-days/month/{month}": "Goetic by ruling month.",
            "goetia/ruling-days/sign/{sign}": "Goetic by ruling astrological sign.",
            "goetia/day-night/{cycle}": "Goetic by Day or Night.",
            "goetia/incense/{incense}": "Goetic by ruling incense.",
            "goetia/color/{color}": "Goetic by ruling color.",
            "goetia/metal/{metal}": "Goetic by ruling metal.",
            "goetia/celectial/{celestial}": "Goetic by ruling planet."
        },
        "links": {
            "sources": {
                "ars-goetia": "https://ia802801.us.archive.org/34/items/ac_goetia/ac_goetia.pdf",
                "demons-and-demonolatry": "https://demonsanddemonolatry.com/"
            },
            "personal": {
                "github": "https://github.com/LilianCodes/ars-goetia-api/",
                "ko-fi": "https://ko-fi.com/wispydealings"
            }
        }
    }

@app.get("/goetia", summary="Get all Goetics.")
def get_all_goetia():
    return goetia

@app.get("/goetia/id", summary="Get all Goetic ID numbers.")
def get_goetia_ids():
    ids = [demon.get("id", "") for demon in goetia.values()]
    return {"id": ids}

@app.get("/goetia/id/{id}", summary="Get Goetic by Specific ID Number.")
def get_goetia_by_id(id: int):
    return goetia.get(str(id), error_handling("ID not found", q=id))

@app.get("/goetia/name/", summary="Get all Goetics by name.")
def get_all_goetia_names():
    names = [demon.get("name", "") for demon in goetia.values()]
    return names

@app.get("/goetia/name/{name}", summary="Get Goetic by Specific Name")
def get_goetia_by_name(name: str):
    name = name.strip().lower()
    for demon in goetia.values():
        if demon.get("name", "").strip().lower() == name:
            return demon
    return error_handling(f"{name} could not be found", q=name)

@app.get("/goetia/alt-names", summary="Get all Goetics by alternate names")
def get_all_goetia_by_alt_name():
    alt_names = [demon.get("alt-names", "") for demon in goetia.values()]
    return alt_names

@app.get("/goetia/alt-names/{alt_name}", summary="Get Goetic by specific alternate name")
def get_goetia_by_alt_name(alt_name: str):
    alt_name = alt_name.strip().lower()
    for demon in goetia.values():
        alt_names = demon.get("alt-names", "")
        if isinstance(alt_names, str):
            if alt_names.strip().lower() == alt_name:
                return {"alt-names": demon}
        elif isinstance(alt_names, (list, dict)):
            if isinstance(alt_names, dict):
                alt_names_values = alt_names.values()
            else:
                alt_names_values = alt_names
            
            if any(str(name).strip().lower() == alt_name for name in alt_names_values):
                return {"alt-names": demon}
    return error_handling(f"{alt_name} could not be found", q=alt_name)

@app.get("/goetia/ruling-days/month/{month}", summary="Get Goetic by Ruling Month")
def get_ruling_day_by_month(month: str):
    month = month.lower()
    res = []

    for demon in goetia.values():
        ruling_days = demon.get("ruling-days", {})
        demon_month = ruling_days.get("month", "").lower()

        if demon_month == month:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{month} could not be found", q=month)

@app.get("/goetia/ruling-days/sign/{sign}", summary="Get Goetic by Ruling Astrological Sign")
def get_goetia_by_sign(sign: str):
    sign = sign.lower()
    res = []

    for demon in goetia.values():
        ruling_days = demon.get("ruling-days", {})
        demon_sign = ruling_days.get("sign", "").lower()

        if demon_sign == sign:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{sign} could not be found", q=sign)

@app.get("/goetia/ruling-days/day-night/{cycle}", summary="Get Goetic by Day or Night")
def get_goetia_by_day_or_night(cycle: str):
    cycle = cycle.lower()
    res = []

    for demon in goetia.values():
        ruling_days = demon.get("ruling-days", {})
        demon_sign = ruling_days.get("day-or-night", "").lower()

        if demon_sign == cycle:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{cycle} could not be found", q=cycle)

@app.get("/goetia/color/{color}", summary="Get Goetic by Ruling Color")
def get_goetia_by_color(color: str):
    color = color.lower()
    res = []

    for demon in goetia.values():
        rank = demon.get("rank", {})
        demon_color = rank.get("color", "").lower()

        if demon_color == color:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{color} could not be found", q=color)

@app.get("/goetia/rank-name/{rank_name}", summary="Get Goetic by Ruling Rank")
def get_goetia_by_rank(rank_name: str):
    rank_name_lower = rank_name.lower()
    res = []

    for demon in goetia.values():
        rank = demon.get("rank")
        if rank and isinstance(rank, dict):
            rank_val = rank.get("rank-name")
            if rank_val and rank_val.lower() == rank_name_lower:
                res.append(demon)

    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{rank_name} could not be found", q=rank_name)

@app.get("/goetia/incense/{incense}", summary="Goetic by Rank Incense")
def get_goetia_by_incense(incense: str):
    incense = incense.strip().lower()
    res = []

    for demon in goetia.values():
        rank = demon.get("rank", {})
        demon_incense = rank.get("incense", "").strip().lower()

        if demon_incense == incense:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{incense} could not be found", q=incense)

@app.get("/goetia/metal/{metal}", summary="Get Goetic by Rank Metal")
def get_goetia_by_metal(metal: str):
    metal = metal.strip().lower()
    res = []

    for demon in goetia.values():
        rank = demon.get("rank", {})
        demon_metal = rank.get("metal", "").strip().lower()

        if demon_metal == metal:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{metal} could not be found", q=metal)

@app.get("/goetia/celestial/{celestial}", summary="Get Goetic by Celestial Body")
def get_goetia_by_celestial(celestial: str):
    celestial = celestial.strip().lower()
    res = []

    for demon in goetia.values():
        rank = demon.get("rank", {})
        demon_celestial = rank.get("celestial", "").strip().lower()

        if demon_celestial == celestial:
            res.append(demon)
    
    if res:
        return {"count": len(res), "results": res}
    return error_handling(f"{celestial} could not be found", q=celestial)

@app.get("/goetia/random", summary="Get a random Goetic")
def get_random_goetia():
    if not goetia:
        return {"error": "No entries found"}
    return random.choice(list(goetia.values()))
