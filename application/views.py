from flask import render_template, request, redirect, flash
from application import app, db
from application.forms import AddCountryForm, AddRegionForm, AddEmployeeForm, DeleteForm
from application.models import Country, Region, Employee


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employees', methods=['GET', 'POST'])
def employees_page():
    form = AddEmployeeForm(request.form)
    if form.validate_on_submit():
        return redirect('/employees')
    else:
        employees_list = Employee.query.order_by(Employee.id.desc()).all()
        return render_template('employees.html', form=form, employees=employees_list)


@app.route('/countries', methods=['GET', 'POST'])
def countries_page():
    add_country_form = AddCountryForm(request.form)
    delete_country_form = DeleteForm(request.form)
    if add_country_form.validate_on_submit():
        country = Country.query.filter_by(name=add_country_form.data['country_name']).all()
        if country:
            flash('Данная страна уже есть в базе, страна должна быть уникальна.')
        else:
            db.session.add(Country(name=add_country_form.data['country_name']))
            db.session.commit()
        return redirect('/countries')
    else:
        countries_list = Country.query.order_by(Country.name).all()
        return render_template(
            'countries.html',
            add_country_form=add_country_form,
            delete_country_form=delete_country_form,
            countries=countries_list
        )


@app.route('/delete_country/<int:country_id>', methods=['POST'])
def delete_country(country_id):
    country = Country.query.filter_by(id=country_id).one()
    db.session.delete(country)
    db.session.commit()
    return redirect('/countries')


@app.route('/regions', methods=['GET', 'POST'])
def regions_page():
    add_region_form = AddRegionForm(request.form)
    add_region_form.country_id.choices = [
        (country.id, country.name) for country in Country.query.order_by('name').all()
    ]
    delete_region_form = DeleteForm(request.form)
    if add_region_form.validate_on_submit():
        region = Region.query.filter(
            Region.country_id == add_region_form.data['country_id']
        ).filter(
            Region.name == add_region_form.data['region_name']
        ).all()
        if region:
            flash('Данный регион уже есть в базе, регион должен быть уникален.')
        else:
            db.session.add(Region(
                name=add_region_form.data['region_name'],
                country_id=add_region_form.data['country_id']
            ))
            db.session.commit()
        return redirect('/regions')
    else:
        regions_list = db.session.query(Region, Country)\
            .join(Country, Country.id == Region.country_id).order_by(Region.name).all()

        regions_dict = {region.Country.name: [] for region in regions_list}

        for region in regions_list:
            regions_dict[region.Country.name].append(region.Region)

        return render_template(
            'regions.html',
            add_region_form=add_region_form,
            delete_region_form=delete_region_form,
            regions=regions_list,
            regions_dict=regions_dict
        )


@app.route('/delete_region/<int:region_id>', methods=['POST'])
def delete_region(region_id):
    region = Region.query.filter_by(id=region_id).one()
    db.session.delete(region)
    db.session.commit()
    return redirect('/regions')


@app.route('/addresses')
def addresses_page():
    return render_template('/addresses.html')
