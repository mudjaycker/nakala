export interface T_Todo {
  title: string;
  text: string;
  importance: number;
  date?: string;
}

export interface T_Py {
  get: () => Promise<T_Todo[]>;
  create: (data: T_Todo) => Promise<null>;
}
