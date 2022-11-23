# To run file from MiniProject folder use python -m test.test_case
from src.functions_projects import add_Item_List,add_courier_info,del_Item_List,update_courier_info

def test_add_Item_List():
    #Assemble
    str_item = "coke"
    str_item_price = "1.0" 
    exiting_list = [{"name":"Fanta","price":"1.1"}]
    expected = [{"name":"Fanta","price":"1.1"},{"name":"coke","price":"1.0"}]
    
    #Act
    actual = add_Item_List(str_item,str_item_price,exiting_list)

    #Assert
    assert expected == actual

def test_add_courier_info():
    
    # Assemble
    str_courier_name = "Kane"
    str_courier_phone = "021-36942317"
    exiting_list = [{"name":"Jane","phone":"021-36942317"}]
    expected = [{'name': 'Jane', 'phone': '021-36942317'}, {'name': 'Kane', 'phone': '021-36942317'}]
    #Act
    actual = add_courier_info(str_courier_name,str_courier_phone,exiting_list)

    #Assert
    assert expected == actual

def test_del_Item_List():
    #Assemble
    item_index = 1
    existing_list = [{'name': 'Fanta', 'price': '0.8'},{'name': 'Coke', 'price': '0.9'},{'name': 'Water', 'price': '0.4'}]
    expected = [{'name': 'Fanta', 'price': '0.8'},{'name': 'Water', 'price': '0.4'}]
    
    #Act
    actual = del_Item_List(item_index,existing_list)
    
    #Assert
    assert expected == actual

def test_update_courier_info():
    #Assemble
    courier_index = 0
    courier_name = 'Subha'
    courier_ph = '074198520'
    exiting_list = [{'name': 'Jane','phone': '07465655'}]
    expected = [{'name': 'Subha','phone': '074198520'}]
    #Act
    actual = update_courier_info(courier_index,courier_name,courier_ph,exiting_list)

    #Assert
    assert expected == actual
    
#calling func
test_add_Item_List()

#calling func
test_add_courier_info()

#calling func
test_del_Item_List()

#calling func
test_update_courier_info()