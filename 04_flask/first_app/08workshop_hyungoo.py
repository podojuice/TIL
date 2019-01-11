from flask import Flask, jsonify

workshop_hyungoo = Flask(__name__)

a = {
        'apple': '사과'
    }

@workshop_hyungoo.route('/dictionary/<string:word>')
def my_dict(word):
    if word in a.keys():
        return f'{word}은(는) {a[word]}!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'
    




if __name__ == '__main__':
    workshop_hyungoo.run(debug=True)