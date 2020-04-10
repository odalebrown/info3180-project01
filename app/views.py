"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, datetime
from app import app, db 
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from forms import UploadForm
from models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    form = UploadForm()

    if request.method == 'POST':
        # Get validated data from form
        if form.validate_on_submit():
            
            firstname = form.firstname.data  
            lastname = form.lastname.data
            gender = form.gender.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            dateCreated = str(datetime.date.today())
            
            profilepic = form.profilePic.data
            imagename = secure_filename(profilepic.filename)
            profilepic.save(os.path.join(app.config['UPLOAD_FOLDER'],imagename))
        
            user = UserProfile(firstname, lastname, gender, email, location, biography, imagename, dateCreated)
            db.session.add(user)
            db.session.commit()
            
           
            flash('User successfully added')
            return redirect(url_for('profile'))
    flash_errors(form)
    return render_template('profile.html', form=form)

@app.route('/profiles')
def allprofile():
    allusers = UserProfile.query.all()
    if allusers is not None:
        return render_template("profiles.html", users=allusers)
        
    return redirect(url_for("home"))

@app.route('/profile/<userid>', methods=['POST', 'GET'])
def userprofile(userid):
    user = UserProfile.query.filter_by(userid=userid).first()
    if user is not None:
        return render_template('userprofile.html',user=user)
        
    return redirect(url_for("home")) 
    
 
def dateinfo():
    return datetime.date().strftime("%B, %d,%Y")
	
    
def get_uploaded_images():
    uploads = []
    for cwd, subdir, files in os.walk('./app/static/uploads/'):
        for file in files:
            print os.path.join(subdir, file) 
            uploads.append(file)
    return uploads
    

###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
