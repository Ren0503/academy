import {
    createAsyncThunk,
    createSlice,
} from '@reduxjs/toolkit'

import { Course } from 'interfaces'
import { baseUrl } from 'utils'

export const listTopCourses = createAsyncThunk<Course[], void>('COURSE_TOP', async () => {
    const response = await fetch(`${baseUrl}/api/courses/top/`)
    const data = await response.json()
    if (!response.ok) {
        throw new Error(data?.message ?? response.statusText)
    }
    return data as Course[]
})

export type CourseTopRatedState = {
    loading: boolean
    courses: Course[]
    error?: string
}

const initialCourseTopRatedState: CourseTopRatedState = {
    loading: false,
    courses: [],
}

export const courseTopSlice = createSlice({
    name: 'courseTop',
    initialState: initialCourseTopRatedState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(listTopCourses.pending, (state) => {
            state.loading = true
            state.courses = []
            state.error = undefined
        })
        builder.addCase(listTopCourses.fulfilled, (state, { payload }) => {
            state.loading = false
            state.courses = payload
        })
        builder.addCase(listTopCourses.rejected, (state, action) => {
            state.loading = false
            state.error = action.error.message
        })
    },
})