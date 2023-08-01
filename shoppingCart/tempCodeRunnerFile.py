if user_id is not None:
        filename = f"static/shoppingCart.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing_data = json.load(f)
                existing_data.append(items_list)
        else:
            existing_data = [items_list]

        with open(filename, 'w') as f:
            json.dump(existing_data, f)
            
    return jsonify(items_list)