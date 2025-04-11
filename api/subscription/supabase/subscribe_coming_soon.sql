create table
  public.subscribe_coming_soon (
    created_at timestamp without time zone not null default now(),
    email_id character varying not null default 'NULL'::character varying,
    constraint subscribe_coming_soon_pkey primary key (email_id),
    constraint subscribe_coming_soon_email_id_key unique (email_id)
  ) tablespace pg_default;