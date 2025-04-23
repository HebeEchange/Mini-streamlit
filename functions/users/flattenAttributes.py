def flatten_attributes(data):
    flattened_data = []
    for item in data:
        flat_item = item.copy()
        attributes = flat_item.pop("attributes", {})
        profile = attributes.pop("profile", {})
        permissions = attributes.pop("permissions", {})
        public_data = profile.pop("publicData", {})
        protected_data = profile.pop("protectedData", {})

        # Fusionner les données imbriquées dans l'élément principal
        flat_item.update(attributes)
        flat_item.update(profile)
        flat_item.update(permissions)
        flat_item.update(public_data)
        flat_item.update(protected_data)
        flattened_data.append(flat_item)
    return flattened_data