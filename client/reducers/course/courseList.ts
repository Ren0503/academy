import {
    createAsyncThunk,
    createSlice,
} from '@reduxjs/toolkit'

import { Course, CourseList } from 'interfaces'
import { baseUrl } from 'utils'

export const listCourses = createAsyncThunk<
    CourseList,
    { keyword: string; pageNumber?: number }
>('COURSE_LIST', async (args) => {
    const { keyword } = args
    const pageNumber = args.pageNumber ?? 1
    const response = await fetch(
        `${baseUrl}/api/courses?keyword=${keyword ?? ''}&page=${pageNumber}`
    )
    const data = await response.json()
    if (!response.ok) {
        throw new Error(data?.message ?? response.statusText)
    }
    return data as CourseList
})

export type CourseListState = {
    loading: boolean
    courses: Course[]
    error?: string
    page: number
    pages: number
}

const initialCourseListState: CourseListState = {
    loading: false,
    courses: [],
    page: 1,
    pages: 1,
}

export const courseListSlice = createSlice({
    name: 'courseList',
    initialState: initialCourseListState,
    reducers: {},
    extraReducers: (builder) => {
        builder.addCase(listCourses.pending, (state) => {
            state.loading = true
            state.courses = []
            state.page = 1
            state.pages = 1
        })
        builder.addCase(listCourses.fulfilled, (state, { payload }) => {
            state.loading = false
            state.courses = payload.courses
            state.pages = payload.pages
            state.page = payload.page
        })
        builder.addCase(listCourses.rejected, (state, action) => {
            state.loading = false
            state.error = action.error.message
        })
    },
})