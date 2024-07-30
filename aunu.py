time_zone_mapping = {
    'Australia/Canberra': 'Australia/Sydney',
    # other mappings can be added here
}

# Usage example:
original_time_zone = 'Australia/Canberra'
mapped_time_zone = time_zone_mapping.get(original_time_zone, original_time_zone)
print(mapped_time_zone)  # Output: Australia/Sydney
