def format_data_for_excel(peoples):
    people_str_list = ["given,family,title"]
    for people in peoples:
        given_name = people["given_name"]
        fam_name = people["family_name"]
        title = people["title"]
        people_str_list.append(f"{given_name},{fam_name},{title}")
    return people_str_list
