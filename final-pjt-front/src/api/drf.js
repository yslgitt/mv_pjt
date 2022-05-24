const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
// const ARTICLES = 'articles/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',

    currentUserInfo: () => HOST + ACCOUNTS + 'user/',

    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },

  movies: {
    movies: () => HOST + MOVIES,
    movie: movieId => HOST + MOVIES + `${movieId}/`,
    reviews: movieId => HOST + MOVIES + `${movieId}/` + 'review/',
    review: (movieId, reviewPk) => HOST + MOVIES + `${movieId}/` + 'review/' `${reviewPk}/` ,
    likeReview: (movieId, reviewPk) => HOST + MOVIES + `${movieId}/` + 'review/' `${reviewPk}/` + 'like/' ,
    recommendationWatch: () => HOST + MOVIES + 'recommendation/' + 'watch/',
    recommendationNetflix: () => HOST + MOVIES + 'recommendation/' + 'netflix/',
    recommendationWatcha: () => HOST + MOVIES + 'recommendation/' + 'watcha/',
    recommendationWavve: () => HOST + MOVIES + 'recommendation/' + 'wavve/',
    recommendationDisney: () => HOST + MOVIES + 'recommendation/' + 'disney/',
  },

  // articles: {

  // }
}
