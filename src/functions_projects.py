
def add_Item_List(str_item, str_item_price, exiting_list):
    exiting_list.append({"name": str_item, "price": str_item_price})
    return exiting_list

def add_courier_info(str_courier_name, str_courier_phone, exiting_list):
    exiting_list.append({"name": str_courier_name, "phone": str_courier_phone})
    return exiting_list

def del_Item_List(item_index, exiting_list=[]):
    exiting_list.pop(item_index)
    return exiting_list

def update_courier_info(courier_index, courier_name, courier_ph, exiting_list=[]):
    exiting_list[courier_index]["name"] = courier_name
    exiting_list[courier_index]["phone"] = courier_ph
    return exiting_list
