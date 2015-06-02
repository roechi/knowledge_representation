import simplegraph.py

bg = simplegraph.SimpleGraph()
bg.load('business_triples.csv')

bg.query([
('?company','headquarters','New_York_New_York'),
('?company','industry','Investment Banking'),
('?company','contributor','?company'),
('?contribution','recipient','Orrin Hatch'),
('?contribution','amount','?dollars')
])


mg = simplegraph.SimpleGraph()
mg.load('movies.csv')

mg.query([
('?actor', 'name', 'Harrison Ford'),
('?director', 'name', 'Steven Spielberg'),
('?movie', 'starring', '?actor'),
('?movie', 'directed_by', '?director'),
('?movie', 'name', '?name')
])