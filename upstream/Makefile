DJANGO_REGISTRATION_RELEASE=b360801eae96 # 2009-06-16 tip http://bitbucket.org/ubernostrum/django-registration/

init: .gitignore
	cd .. && git submodule update --init
	hg clone -r $(DJANGO_REGISTRATION_RELEASE) http://bitbucket.org/ubernostrum/django-registration/

.gitignore:
	echo .gitignore > .gitignore
	echo django-registration >> .gitignore
