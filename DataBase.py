from peewee import *
import time
import Dictionary

db = SqliteDatabase('Telegram.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    first_name = CharField()
    last_name = CharField()
    user_id = IntegerField(unique=True)
    date = DateField(time.time())
    phone_number = CharField()
    lang = CharField()
    SUMKA_INKASSATOR_30x40 = IntegerField()
    SUMKA_INKASSATOR_40x50 = IntegerField()
    SUMKA_INKASSATOR_40x70 = IntegerField()
    MESHOK_INKASSATOR_60_90 = IntegerField()
    MESHOK_EVACUATION_75x115 = IntegerField()
    SUMKA_FOR_KASSET_ATM_5_CELL = IntegerField()

    class Meta:
        database = db
        table_name = "Users"


class Goods(BaseModel):
    bag_name = CharField(unique=True)
    price = DoubleField()
    size = CharField()

    class Meta:
        database = db
        table_name = "Goods"


class Language(BaseModel):
    uz = CharField(unique=True)
    ru = CharField(unique=True)
    var_name = CharField(unique=True)

    class Meta:
        database = db
        table_name = "Languages"


db.connect()
db.create_tables([User, Goods, Language])
for key in range(16):
    Language.create(var_name=Dictionary.var_name[key], ru=Dictionary.ru[key], uz=Dictionary.uz[key])

# "SELECT_BAG",
# "SELECTED_LANG",
# "WELCOME",
# "MESHOK_INKASSATOR",
# "SUMKA_INKASSATOR",
# "MESHOK_EVACUATION",
# "BACK",
# "HOME",
# "GOODS",
# "FEEDBACK",
# "BIN",
# "HISTORY",
# "SUMKA_FOR_KASSET_ATM_5_CELL",
# "DELETE_BAGS",
# "HISTORY_BTN_PRESSED",
# "BIN_BTN_PRESSED",
# "FEEDBACK_BTN_PRESSED"
