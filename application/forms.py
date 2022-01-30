from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, validators, IntegerField, BooleanField


class AddCountryForm(FlaskForm):
    country_name = StringField('Страна', validators=[validators.InputRequired(message='Введите название страны')])
    submit = SubmitField('Добавить')


class AddRegionForm(FlaskForm):
    country_id = SelectField(
        'Страна',
        coerce=int,
        validators=[validators.InputRequired(message='Введите название страны')]
    )
    region_name = StringField('Регион', validators=[validators.InputRequired(message='Введите название региона')])
    submit = SubmitField('Добавить')


class DeleteForm(FlaskForm):
    submit = SubmitField('Удалить')


class AddAddressForm(FlaskForm):
    country_name = StringField('Страна', validators=[validators.InputRequired(message='Введите название страны')])
    region_name = StringField('Регион', validators=[validators.InputRequired(message='Введите название региона')])
    city = StringField('Город', validators=[validators.InputRequired(message='Введите название города')])
    street = StringField('Улица', validators=[validators.InputRequired(message='Введите название улицы')])
    house_number = IntegerField('Номер дома', validators=[validators.InputRequired(message='Введите номер дома')])
    apartments_number = IntegerField('Номер квартиры', validators=[validators.Optional()])
    submit = SubmitField('Добавить')


class AddEmployeeForm(FlaskForm):
    surname = StringField('Фамилия', validators=[validators.InputRequired()])
    name = StringField('Имя', validators=[validators.InputRequired()])
    patronymic = StringField('Отчество')
    birth_date = DateField('Дата рождения', validators=[validators.InputRequired()])
    gender = SelectField('Пол', choices=('Мужской', 'Женский'), validators=[validators.InputRequired()])
    birth_place = AddAddressForm
    address = AddAddressForm
    military_duty = BooleanField()
    # autobiography =
    # job =
    submit = SubmitField('Добавить работника')
