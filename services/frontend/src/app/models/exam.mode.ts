export class Exam {
    constructor(
        public title: string,
        public description: string,
        public id?: number,
        public updated_at?: Date,
        public created_at?: Date,
        public last_updated_by?: string,
    ) {}
}