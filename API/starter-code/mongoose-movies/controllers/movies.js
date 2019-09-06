var Movie = require("../models/movie");
var Performer = require("../models/performer");

module.exports = {
  index,
  show,
  new: newMovie,
  create,
  deleteMovie
};

function deleteMovie(req, res) {
  Movie.findByIdAndRemove(req.params.id).then(function(err, movies) {
    res.status(200).json(movies);
  });
}
// Movie.create(req.body).then(function(movie) {
//   res.status(201).json(movie);

function index(req, res) {
  Movie.find({})
    .then(function(movies) {
      res.status(200).json(movies);
    })
    .catch(function(err) {
      res.status(500).json(err);
    });
}

function show(req, res) {
  Movie.findById(req.params.id)
    .populate("cast")
    .exec(function(err, movies) {
      // Performer.find({}).where('_id').nin(movie.cast)
      Performer.find({ _id: { $nin: movie.cast } }).exec(function(
        err,
        performers
      ) {
        console.log(performers);
        res.render("movies/show", {
          title: "Movie Detail",
          movies,
          performers
        });
      });
    });
}

function newMovie(req, res) {
  res.render("movies/new", { title: "Add Movie" });
}

function create(req, res) {
  Movie.create(req.body).then(function(movies) {
    res.status(201).json(movies);
  });
  // convert nowShowing's checkbox of nothing or "on" to boolean
  // req.body.nowShowing = !!req.body.nowShowing;
  // for (let key in req.body) {
  //   if (req.body[key] === "") delete req.body[key];
  // }
  // var movie = new Movie(req.body);
  // movie.save(function(err) {
  //   if (err) return res.redirect("/movies/new");
  //   // res.redirect('/movies');
  //   res.redirect(`/movies/${movie._id}`);
  // });
}
