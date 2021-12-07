import {
    createAsyncThunk,
    createSlice,
} from '@reduxjs/toolkit'

import { Course } from 'interfaces'
import { baseUrl } from 'utils'

export const detailCourse = createAsyncThunk<Course, string>(
    'COURSE_DETAILS',
    async (courseId) => {
        const response = await fetch(`${baseUrl}/api/courses/${courseId}`)
        const data = await response.json()
        if (!response.ok) {
            throw new Error(data?.message ?? response.statusText)
        }
        return data as Course
    }
)

export type CourseDetailsState = {
    loading: boolean
    course?: Course
    error?: string
}

const initialCourseDetailsState: CourseDetailsState = {
    loading: false,
}

export const courseDetailsSlice = createSlice({
    name: 'courseDetails',
    initialState: initialCourseDetailsState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(detailCourse.pending, (state) => {
            state.loading = true
        })
        builder.addCase(detailCourse.fulfilled, (state, { payload }) => {
            state.loading = false
            state.course = payload
        })
        builder.addCase(detailCourse.rejected, (state, action) => {
            state.loading = false
            state.error = action.error.message
        })
    },
})