# PRE-ENTREGA 2
# Modelando la base de datos de un Blog con Python


# PERFIL DEL AUTOR

perfil_autor = {
    "nombre": "José Mercado",
    "bio": "Estudiante de desarrollo web y creador de contenido sobre programación.",
    "especialidad": "Desarrollo Web",
    "redes_sociales": [
        "@jose_dev",
        "@jose_web"
    ]
}


# ESTADOS POSIBLES DE LOS POSTS
# Tupla: sus valores son fijos

estados_post = (
    "borrador",
    "publicado",
    "archivado"
)


# ETIQUETAS DEL BLOG
# Python está repetido intencionalmente para comprobar
# que los sets eliminan elementos duplicados.

etiquetas_blog = {
    "Python",
    "Desarrollo Web",
    "HTML",
    "CSS",
    "Python"
}


# LISTA DE POSTS

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },

    {
        "id": 2,
        "titulo": "Aprendiendo desarrollo web",
        "autor": perfil_autor,
        "categoria": "Desarrollo Web",
        "tags": ["HTML", "CSS", "Web"],
        "estado": "borrador"
    },

    {
        "id": 3,
        "titulo": "Estructuras de datos en Python",
        "autor": perfil_autor,
        "categoria": "Programación",
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    }
]


# VERIFICACIÓN DE DATOS

print(
    "Autor del segundo post:",
    posts[1]["autor"]["nombre"]
)

print("Lista de posts guardados:")
print(posts)


# VERIFICACIÓN DE TIPOS

print("Tipo de estados_post:", type(estados_post))
print("Tipo de etiquetas_blog:", type(etiquetas_blog))