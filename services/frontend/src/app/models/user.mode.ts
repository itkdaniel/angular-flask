export class User{
    constructor (
        public username: string,
        public password: string,
        public salt?: string,
        public id?: number,
        public created_at?: Date,
        public updated_at?: Date,
        public last_updated_by?: string
    ) {}
}