export interface Course {
	_id: string
	name: string
	image: string
	description: string
	category: string
	participants: number
	rating: number
	numReviews: number
	reviews: Array<Review>
    createdAt: string
}

export interface Review {
	_id: string
	user: string
	name: string
	rating: number
	comment: string
	createdAt: string
}

export interface CourseList {
	courses: Course[]
	pages: number
	page: number
}

export interface CreateReviewInput {
	rating: number
	comment: string
}