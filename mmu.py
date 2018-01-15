import sys

# 初始化虚拟内存
def init_virtual_memory():
    _virtual_memory = []
    for i in range(10):
        for j in range(20):
            _virtual_memory.append({i: j})
    return _virtual_memory

# 初始化页表
def init_page_table():
    _page_table = []
    for i, j in zip(range(10), range(10, 20)):
        _page_table.append({i: j})
    return _page_table

# 初始化页表寄存器，返回页表项长度和页表指针（雾）
def init_page_table_register(_virtual_memory, _page_table):
    page_number = set()
    for idict in _virtual_memory:
        if list(idict.keys())[0] not in page_number:
            page_number.add(list(idict.keys())[0])
    return [len(page_number), _page_table]

def error_process():
    print ("error")
    sys.exit()

def handle(_page_number, _page_address, _page_table_register, _page_table):
    if _page_number >= _page_table_register[0]:
        error_process()
    for idict in _page_table:
        if list(idict.keys())[0] == _page_number:
            break
    
    # int(list(idict.values())[0]) + page_address
    print("\nphysical memory:\n\tpage number:" + str(list(idict.values())[0]) + "\n\tpage address:" + str(_page_address))

    
if __name__ == '__main__':
    virtual_memory = init_virtual_memory()
    print (virtual_memory)

    page_table = init_page_table()
    print (page_table)

    page_table_register = init_page_table_register(virtual_memory, page_table)
    print (page_table_register)

    page_number = int(input("Input the page number: "))
    page_address = int(input("Input the page address: "))
 
    handle(page_number, page_address, page_table_register, page_table)
    