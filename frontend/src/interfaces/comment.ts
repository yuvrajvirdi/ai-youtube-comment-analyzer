export interface IComment {
	author: string;
	comment: string;
	isSpam: boolean;
	likeCount: number;
	publishedDate: string;
	sentiment: string;
	topics: string[];
	type: string;
}