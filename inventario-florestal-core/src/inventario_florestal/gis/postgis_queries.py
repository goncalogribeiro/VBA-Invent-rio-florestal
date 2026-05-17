from __future__ import annotations


POSTGIS_EXEMPLOS = {
    "buffer": "SELECT ST_Buffer(geom, 50) FROM talhoes;",
    "intersecao": "SELECT ST_Intersects(a.geom, b.geom) FROM talhoes a, app b;",
    "area": "SELECT ST_Area(geom) FROM talhoes;",
    "distancia": "SELECT ST_Distance(a.geom, b.geom) FROM parcelas a, estradas b;",
}


DASHBOARDS_ESPACIAIS = {
    "produtividade": "Mapa espacial de produtividade",
    "risco": "Mapa espacial de risco",
    "carbono": "Mapa espacial de carbono",
    "fsc": "Mapa espacial de compliance FSC",
}


class ErroPostGIS(Exception):
    pass



def listar_operacoes_postgis() -> list[str]:
    """
    Lista operações espaciais suportadas.
    """

    return list(POSTGIS_EXEMPLOS.keys())



def listar_dashboards_espaciais() -> list[str]:
    """
    Lista dashboards GIS previstos.
    """

    return list(DASHBOARDS_ESPACIAIS.keys())
