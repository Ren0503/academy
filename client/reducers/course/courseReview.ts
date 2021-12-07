import {
    createAsyncThunk,
    createSlice,
} from '@reduxjs/toolkit'

import { CreateReviewInput } from 'interfaces'
import { baseUrl } from 'utils'

import { ReduxState } from 'store'
import { UserLoginState } from 'reducers/user'

export const createCourseReview = createAsyncThunk<
    void,
    CreateReviewInput & { courseId: string }
>(
    'COURSE_CREATE_REVIEW',
    async (payload: CreateReviewInput & { courseId: string }, thunkAPI) => {
        const state: ReduxState = thunkAPI.getState()
        const userLogin: UserLoginState = state.userLogin
        const token = userLogin.userInfo?.token
        const { courseId } = payload

        if (!token) {
            throw new Error('no user login token')
        }
        const response = await fetch(`${baseUrl}/api/courses/${courseId}/reviews/`, {
            method: 'POST',
            body: JSON.stringify(payload),
            headers: {
                'Content-Type': 'application/json',
                Authorization: 'Bearer ' + token,
            },
        })
        const data = await response.json()
        if (!response.ok) {
            throw new Error(data?.message ?? response.statusText)
        }
    }
)

export interface CourseCreateReviewState {
    loading: boolean
    success?: boolean
    error?: string
}

const initialCourseCreateReviewState: CourseCreateReviewState = { loading: false }


export const createCourseReviewSlice = createSlice({
    name: 'courseCreateReview',
    initialState: initialCourseCreateReviewState,
    reducers: {
        reset: (state) => {
            state.error = undefined
            state.loading = false
            state.success = false
        },
    },
    extraReducers: (builder) => {
        builder.addCase(createCourseReview.pending, (state) => {
            state.loading = true
            state.error = undefined
        })
        builder.addCase(createCourseReview.fulfilled, (state) => {
            state.loading = false
            state.success = true
        })
        builder.addCase(createCourseReview.rejected, (state, action) => {
            state.loading = false
            state.error = action.error.message
        })
    },
})