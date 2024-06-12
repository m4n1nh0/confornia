"""Adversary response implementation."""

json = {
    "id": "int",
    "iso_name": "str",
    "description": "str",
    "reference": "str",
    "excluded": "true"
}

questions_responses = {
    "all": {
        401: {"description": "Não autorizado."},
        200: {
            "description": "Sucesso.",
            "content": {
                "application/json": {
                    "example": [json]
                }
            },
        }
    },

    "single": {
        200: {
            "description": "Sucesso.",
            "content": json
        },
        404: {'description': "Registro não encontrado."},
    },

    "register": {
        200: {
            "description": "Cadastrado com sucesso.",
            "content": json
        },
        404: {'description': "Registro não encontrado."},
        406: {'description': 'Registro já cadastrado anteriormente.'}
    },

    "update": {
        200: {
            "description": "Atualizado com sucesso.",
            "content": json
        },
        404: {'description': 'Registro não encontrado.'},
        406: {'description': 'Registro já cadastrado anteriormente.'}
    },

    "validate": {
        200: {
            "description": "Sucesso.",
            "content": json
        },
        404: {'description': 'Registro não encontrado.'},
    },

    "delete": {
        404: {'description': 'Registro não encontrado.'},
    }

}
