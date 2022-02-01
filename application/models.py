from application import db


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    regions = db.relationship('Region', backref='countries')

    def __repr__(self):
        return '<Country %r>' % self.name


class Region(db.Model):
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    __table_args__ = (db.UniqueConstraint('country_id', 'name', name='_country_region_uc'),)

    def __repr__(self):
        return '<Region %r>' % self.name


class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    house_number = db.Column(db.Integer, nullable=False)
    apartments_number = db.Column(db.Integer)

    def __repr__(self):
        return '<Address %r, %r, %r, %r, %r %r>' % (
            self.country,
            self.region,
            self.city,
            self.street,
            self.house_number,
            self.apartments_number
        )


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<Department %r>' % self.name


class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    salary = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return '<Job %r>' % self.post


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50))
    birth_date = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20))
    birth_place = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    military_duty = db.Column(db.Boolean, nullable=False)
    autobiography = db.Column(db.Text)
    job = db.Column(db.Integer, db.ForeignKey('jobs.id'))

    def __repr__(self):
        return '<Employee %r %r>' % (self.surname, self.name)
