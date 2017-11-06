# imports - module imports
import schema

def test_check():
	assert schema.check('Thing', dict(
		url = 'http://bit.ly/2fbwx4m'
	)) == True
	assert schema.check('Thing', dict(
		foo = 'bar'
	)) == False