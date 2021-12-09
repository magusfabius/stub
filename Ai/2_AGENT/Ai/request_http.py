import requests

dev_mode = True

current_error_code = 0 # no errors, strange ;) positive or negative loop? ?
current_error_txt = ""
current_status_code = 201
current_status_txt = ""


def make_brutal_request(url):
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    r.status_code
    r.headers['content-type']

def make_qr_request(url, query, uery):
    # query_ex = [1, 0, "Ciao", "2"];
    r = requests.get(url, auth=('user', 'pass'))
    r.status_code
    r.headers['content-type']

def make_call(url, id):
    # emily emilywhite9@gmail.com
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    r.status_code
    r.headers['content-type']

def update_status(new_status):
    if dev_mode:
        error_answer = input("Status changed. Wanna have log? (Y/n/s)")
        

        if error_answer == "":
            

    if current_error_code == 0:
        
    else:
        current_status_code = 
        print(current_error_code)



