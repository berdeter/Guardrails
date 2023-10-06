from nemoguardrails import LLMRails, RailsConfig

# Lisons les fichiers de configuration
with open("rails.co") as f:
    colang = f.read()
with open("config.yaml") as f:
    yaml = f.read()

config = RailsConfig.from_content(yaml_content=yaml, colang_content=colang)


# Initialisons les rails
rails = LLMRails(config)

# Ask tu generate a massage in answer to the question "Comment-vas-tu ?" to the AI via the rail
rails.generate_message("Comment vas-tu ?")

