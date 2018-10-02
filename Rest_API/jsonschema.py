notes_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "pattern": "^[A-G][#b]?[0-9]$"
            },
            "duration": {
                "type": "string",
                "pattern": "^\d+\/\d+$"
            }
        },
        "required": ["name", "duration"]
    }
}

notes_example = [{"name": "C#4", "duration": "1/4"},
                 {"name": "A4", "duration": "1/32"}]